#!/usr/bin/env python3
import subprocess
import sys

def check_service_status(service_name):
    try:
        # Проверяем статус службы
        result = subprocess.run(['systemctl', 'is-active', service_name], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip() == 'active':
            return True
        return False
    except Exception as e:
        print(f"Ошибка при проверке статуса службы: {e}")
        return False

def start_service(service_name):
    try:
        # Запускаем службу
        result = subprocess.run(['systemctl', 'start', service_name], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Служба {service_name} успешно запущена")
            return True
        else:
            print(f"Ошибка при запуске службы: {result.stderr}")
            return False
    except Exception as e:
        print(f"Ошибка при запуске службы: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Использование: python3 check_and_start_service.py <имя_службы>")
        sys.exit(1)
    
    service_name = sys.argv[1]
    
    if check_service_status(service_name):
        print(f"Служба {service_name} уже запущена")
    else:
        print(f"Служба {service_name} не запущена, попытка запуска...")
        start_service(service_name)

if __name__ == "__main__":
    main()
# chmod +x check_and_start_service.py
# sudo ./check_and_start_service.py mysqld
