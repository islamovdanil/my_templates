#!/bin/bash

# Функция проверки сертификатов
check_certificates() {
    local dir="$1"
    echo "Проверка сертификатов в директории: $dir"
    
    # Поиск файлов сертификатов
    for file in $(find "$dir" -type f -name "*.crt" -o -name "*.pem" -o -name "*.cer"); do
        echo "---"
        echo "Файл сертификата: $file"
        
        # Получение информации о сертификате
        echo "Информация о сертификате:"
        openssl x509 -in "$file" -noout -text 2>/dev/null | grep -E 'Validity|Not Before|Not After'
        
        # Расчет оставшегося времени
        expires=$(openssl x509 -in "$file" -noout -enddate 2>/dev/null | cut -d= -f2)
        if [ -n "$expires" ]; then
            remaining=$(date -d "$expires" +%s)
            now=$(date +%s)
            diff=$((remaining - now))
            days=$((diff / 86400))
            echo "Осталось дней до истечения: $days"
        fi
    done
}

# Функция проверки открытых ключей
check_public_keys() {
    local dir="$1"
    echo "Проверка открытых ключей в директории: $dir"
    
    # Поиск файлов открытых ключей
    for file in $(find "$dir" -type f -name "*.pub"); do
        echo "---"
        echo "Файл открытого ключа: $file"
        
        # Вывод информации о ключе
        echo "Информация о ключе:"
        ssh-keygen -lf "$file"
    done
}

# Основные директории для проверки
CERT_DIRS=(
    "/etc/ssl/certs"
    "/usr/local/share/ca-certificates"
    "/root/.ssh"
    "/home/*/.ssh"
)

# Проверка сертификатов
echo "Проверка сертификатов..."
for dir in "${CERT_DIRS[@]}"; do
    check_certificates "$dir"
done

# Проверка открытых ключей
echo "Проверка открытых ключей..."
for dir in "${CERT_DIRS[@]}"; do
    check_public_keys "$dir"
done
