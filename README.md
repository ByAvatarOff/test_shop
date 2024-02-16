## Алгоритм запуска
### Скачать проект
```shell
git clone https://github.com/ByAvatarOff/test_shop.git
cd test_shop
```
### Для удобства запуска оставил файл .env. Оставил SessionAuthentication для удобства тестирование без необходимости отправлять header Authorization. также при запуске основного бэкенда создается супер пользователь username: admin, password: admin
### Создание общей сети для работы контейнеров
```shell
docker network create main_network
```
### Запуск тестов для микросервиса shop
```shell
docker-compose -f docker-compose-tests.yaml up --build
```
### Запуск в фоне микросервиса shop
```shell
docker-compose -f docker-compose-main.yaml create
docker-compose -f docker-compose-main.yaml start
```

### Запуск основного бэкенда (вместе с тестами)
```shell
docker-compose up --build
```
### Запуск основного бэкенда в фоновом режиме
```shell
docker-compose create
docker-compose start
```
### Для тестирование endpoint-ов с авторизацией можно войти в админку django с данными username: admin password: admin


## Endpoint-ы для основного сервиса
### Модуль авторизации, регистрации
### 1)  **[POST]** Регистрация пользователя
### ``` api/auth/register/ ```

### body
```
[
  {
    "username": "test",
    "email": "test@mail.ru",
    "password": "test",
    "repeat_paaaword": "test",
  }
]
```

### 2) **[POST]** Получение jwt токена
### ``` api/auth/token/ ```
### Body
```
{
  "username": "admin",
  "password": "admin"
}
```
### Data
```
{
  "access": "",
  "refresh": "",
}
```

### 3) **[POST]** Обновление jwt токена
### ``` api/auth/token/refresh/ ```

### Body
```
{
  "refresh": "<REFRESH_TOKEN>",
}
```
### Data
```
{
  "access": "",
}
```

### 4) **[GET]** Получение своего профиля
### Header 'Authorization: bearer {access_token}'
### ``` api/auth/user/ ```

### Data
```
{
  "username": "username",
  "email": "email",
}
```
## Модуль запросов к микросервису
### 5) **[GET]** Получение списка товаров
### Header 'Authorization: bearer {access_token}'
### ``` api/shop/items/```

### Data
```
[
  {
    "id": 0,
    "title": "string",
    "description": "string",
    "price": "12.8",
    "origin_country": "string",
    "date_add": "2024-02-16T11:24:24.189Z"
  }
]
```

### 6) **[POST]** Создание товара
### Header 'Authorization: bearer {access_token}'
### ``` api/shop/create_item/ ```

### Body
```
{
  "title": "string",
  "description": "string",
  "price": 12.8,
  "origin_country": "string"
}
```
### Data
```
{
  "id": 0,
  "title": "string",
  "description": "string",
  "price": "string",
  "origin_country": "string",
  "date_add": "2024-02-16T11:25:38.084Z"
}
```

### 7) **[GET]** Получение товара по id
### Header 'Authorization: bearer {access_token}'
### ``` api/shop/get_item/{item_id}/ # item_id - int```

### Data
```
{
  "id": 0,
  "title": "string",
  "description": "string",
  "price": "string",
  "origin_country": "string",
  "date_add": "2024-02-16T11:26:50.871Z"
}
```

### 8) **[PATCH]** Обновление товара по id
### Header 'Authorization: bearer {access_token}'
### ``` api/shop/update_item/{item_id}/ # item_id - int```

### Body
```
{
  "title": "string",
  "description": "string",
  "price": 12.0,
  "origin_country": "string"
}
```
### Data
```
{
  "id": 0,
  "title": "string",
  "description": "string",
  "price": "string",
  "origin_country": "string",
  "date_add": "2024-02-16T11:25:38.084Z"
}
```

### 9) **[DELETE]** Удаление товара по id
### Header 'Authorization: bearer {access_token}'
### ``` api/shop/delete_item/{item_id}/ # item_id - int```

### Data
```
{
  "message": "Success item delete"
}
```

### 10) **[DELETE]** Удаление всех товаров
### Header 'Authorization: bearer {access_token}'
### ``` api/shop/delete_items/```

### Data
```
{
  "message": "Success all items delete"
}
```
