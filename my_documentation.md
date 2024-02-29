# Java Database Connection

This Java program demonstrates how to establish a connection to a MySQL database using the JDBC (Java Database Connectivity) API.

## Code Overview

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/myDatabase";
        String username = "myUsername";
        String password = "myPassword";

        System.out.println("Connecting to database...");

        try (Connection connection = DriverManager.getConnection(url, username, password)) {
            System.out.println("Connected successfully!");
        } catch (SQLException e) {
            throw new IllegalStateException("Cannot connect to the database!", e);
        }
    }
}
```

## Explanation

The program starts by importing the necessary classes from the `java.sql` package.

In the `main` method, it defines the URL, username, and password required to connect to the database. The URL specifies the database server (localhost), the port number (3306), and the database name (myDatabase).

The program then attempts to establish a connection to the database using `DriverManager.getConnection()`. This method returns a `Connection` object, which represents the database connection.

If the connection is successful, it prints "Connected successfully!". If a `SQLException` is thrown (for example, if the connection fails), it throws a new `IllegalStateException` with an appropriate error message.

## Usage

To use this program, replace the URL, username, and password with your actual database credentials. Then, run the program. If the connection is successful, it will print "Connected successfully!". If not, it will throw an exception with an error message.