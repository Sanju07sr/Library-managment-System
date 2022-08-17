# Library-managment-System
Library management system in integration with SQL and flask framework.

Add.html

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Add Book Details</title>
  </head>
  <body>

    <div class="container">
    <h1>Add New Book Details </h1>
    <div class="col-6">
        <form method="POST">
            <input type="text" class="form-control" id="txtName" name="txtName" placeholder="Book Name" required>
            <br>

            <input type="text" class="form-control" id="txtAuthor" name="txtAuthor" placeholder="Author Name" required>
            <br>

            <input type="number" class="form-control" id="txtPrice" name="txtPrice" placeholder="Book Price" required>
            <br>

            <input type="text" class="form-control" id="txtPublication" name="txtPublication" placeholder="Publication Name" required>
            <br>

            <input type="date" class="form-control" id="txtPublicationDate" name="txtPublicationDate" placeholder="Publication Date" required>
            <br>

            <input type="submit" value="Add Book" class="btn btn-primary">
        </form>
    </div>
    </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
  </body>
</html>

index.html

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>

    

    <h1>LIBRARY MANAGMENT SYSTEM</h1>
    
    <div class="container">
      <a href="http://127.0.0.1:5000/add" class="btn
      btn-primary">Add Details</a>
        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Book NAME</th>
                    <th scope="col">Author</th>
                    <th scope="col">Price</th>
                    <th scope="col">Publication</th>
                    <th scope="col">Publication date</th>
                    <th></th>
                    <th scope="col">Edit</th>
                </tr>
            </thead>
            <tbody>
                {% for book in data %}
                <tr>
                    <td>{{book[0]}}</td>
                    <td>{{book[1]}}</td>
                    <td>{{book[2]}}</td>
                    <td>{{book[3]}}</td>
                    <td>{{book[4]}}</td>
                    <td>{{book[5]}}</td>
                    <td>{{book[6]}}</td>
                    <td>
                      <a href=" http://127.0.0.1:5000/update?ID={{book[0]}}" class="btn btn-warning">Update</a>
                      <a href=" http://127.0.0.1:5000/delete?ID={{book[0]}}" class="btn btn-danger">Delete</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
  </body>
</html>

update.html

<h1>LIBRARY MANAGEMENT SYSTEM</h1>

<div class="col-6">
    {% if data %}
    <form method="post">
        <input type="text" class="form-control" id="txtName" name="txtName" placeholder="Book Name" required>
        <br>

        <input type="text" class="form-control" id="txtAuthor" name="txtAuthor" placeholder="Author Name" required>
        <br>

        <input type="number" class="form-control" id="txtPrice" name="txtPrice" placeholder="Book Price" required>
        <br>

        <input type="text" class="form-control" id="txtPb" name="txtPb" placeholder="Publication Name" required>
        <br>

        <input type="date" class="form-control" id="txtPbd" name="txtPbd" placeholder="Publication Date" required>
        <br>
    
        <input type="submit" value="Update Book" class="btn btn-primary">
    </form>
  {% endif %}
  {% if message %}
    <div class="alert alert-info">
      {{message}}
    </div>
    {% endif %}
</div>


![Screenshot (146)](https://user-images.githubusercontent.com/100313227/185193089-f075f5c0-abd5-4d50-8de0-ac1882a001eb.png)
![Screenshot (147)](https://user-images.githubusercontent.com/100313227/185193099-3462627c-9217-4181-97c4-685292245a89.png)
![Screenshot (148)](https://user-images.githubusercontent.com/100313227/185193104-4d3d6b34-016a-459c-8d6b-d1da62943b9d.png)
![Screenshot (149)](https://user-images.githubusercontent.com/100313227/185193108-f2e9b8f8-ce35-4636-bebc-268a5e67ed0d.png)
![Screenshot (150)](https://user-images.githubusercontent.com/100313227/185193111-2268e376-ec9e-4a6c-9344-12c2d13099f6.png)

