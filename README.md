# Тестовое задание

## Установка и запуск через Docker

```bash
git clone https://github.com/e-trp/library.git
cd library
docker-compose up -d

```
## API 
----

* ## **Аутентификация(получения токена)**
  > Аутентификация и взаимодействие с api производится через drf toknen,
  > добавлением в http headers
  >  'Authorization: Token token_string'
  > 

   `api/auth/`

   *method:* `POST` 
  

  ```bash
  {
      "username": string,
      "password": string
  }
  ```

  **Success Response:**

  *Code:* `200`
  ``` bash
  {
    "token": string
  }  
  ```



* ## **Регистрация**


  `api/register/`

  *method:* `POST` 
  

   ```bash
    {
        "username": string,
        "password": string,
        "email": string
    }
  ```
  
  **Success Response:**

  *Code:* `201`
  ``` bash
  {
    "username": string,
    "email": string
  }  
  ```


## Сущности 
----
> Администратору доступны все методы, пользователю только только чтение. Книга с годом публикации больше текущего доступна только администраторам. По сущности Книга доступна фильтрация, поиск и сортировка. При добавлении новой книги должна происходить email-рассылка всем подписчикам

* ## Автор

  *list*

  `api/authors/`

  *method* `GET`

  *object*

  `api/authors/<id>`

  *method* `GET` `PUT` `POST` `DELETE`

  ```bash
  {
  "id": int,
  "first_name": string,
  "mid_name": string,
  "last_name": string
  }
  ```


* ## Книга

  *list*

  `api/books/`

  *method* `GET`

  *object*

  `api/books/<id>`

  *method* `GET` `PUT` `POST` `DELETE`


  `api/books/<id>`
    ```bash
  {
    "id": int,
    "name": string,
    "language": string,
    "publish_date": datetime_iso_str,
    "author": author_id
  }
  ```


* ## Подписчик


  *list*

  `api/subscribers/`

  *method* `GET`

  *object*

  `api/subscribers/<id>`

  *method* `GET` `PUT` `POST` `DELETE`

  ```bash
  {
    "id": int,
    "first_name": string,
    "mid_name": string,
    "last_name": string,
    "email": string
  }
  ```