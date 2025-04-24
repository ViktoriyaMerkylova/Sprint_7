# Sprint_7
Демо для практикума. Тестирование API "Яндекс Самокат"
# О проекте:

Практикум по Page Object, направленный на тестирование веб-приложения «Яндекс.Самокат».



# Запуск тестов

1. Основа для написания автотестов - pytest, selenium
    
2. Установить зависимости:
    
    
    pip install pytest
    pip install selenium

3.Команда для запуска: 
    
    
    pytest -v tests

4.Просмотреть отчет:
 
    Запуск тестов с генерацией от allure 
    pytest --alluredir=allure-results
    
    Просмотр тестов в браузере
    allure serve allure-results

