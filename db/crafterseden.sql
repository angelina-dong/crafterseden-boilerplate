DROP SCHEMA IF EXISTS crafterseden ;
CREATE SCHEMA IF NOT EXISTS crafterseden;
USE crafterseden;

#  drop table YarnProduct, BeadProduct, PaintProduct, Products,
#     Projects, Patterns, Reviews, Orders, OrderDetails, Customers, Suppliers, Shipments;


USE crafterseden;

CREATE TABLE IF NOT EXISTS Suppliers
(
    SupplierID int PRIMARY KEY AUTO_INCREMENT,
    Location   varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Customers
(
    CustomerID int PRIMARY KEY AUTO_INCREMENT,
    Name       varchar(100) NOT NULL,
    Email      varchar(100) NOT NULL UNIQUE,
    Address    varchar(100) NOT NULL,
    Phone      varchar(15)  NOT NULL UNIQUE,
    Username   varchar(50)  NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS YarnProduct
(
    YarnID               int PRIMARY KEY AUTO_INCREMENT,
    ProductName          varchar(100) NOT NULL,
    SkeinLength          numeric      NOT NULL,
    Price                numeric      NOT NULL,
    Fiber                numeric NOT NULL,
    Color                varchar(50)  NOT NULL,
    YarnWeight           numeric NOT NULL,
    NetWeight            numeric      NOT NULL,
    Brand                varchar(100) NOT NULL,
    ManufacturingCountry varchar(100) NOT NULL,
    Photos               varchar(100)
);

CREATE TABLE IF NOT EXISTS BeadProduct
(
    BeadID               int PRIMARY KEY AUTO_INCREMENT,
    ProductName          varchar(100) NOT NULL,
    Material             varchar(100) NOT NULL,
    Price                numeric      NOT NULL,
    Color                varchar(50)  NOT NULL,
    Size                 numeric      NOT NULL,
    Brand                varchar(100) NOT NULL,
    ManufacturingCountry varchar(100) NOT NULL,
    Photos               varchar(100)
);

CREATE TABLE IF NOT EXISTS PaintProduct
(
    PaintID              int PRIMARY KEY AUTO_INCREMENT,
    ProductName          varchar(100) NOT NULL,
    Base                 varchar(100) NOT NULL,
    Ingredients          varchar(500) NOT NULL,
    Price                numeric      NOT NULL,
    Color                varchar(50)  NOT NULL,
    FluidVolume          numeric      NOT NULL,
    Brand                varchar(100) NOT NULL,
    ManufacturingCountry varchar(100) NOT NULL,
    Photos               varchar(100)
);

CREATE TABLE IF NOT EXISTS Products
(
    ProductID    int PRIMARY KEY AUTO_INCREMENT,
    YarnID       int,
    BeadID       int,
    PaintID      int,
    UnitsInStock int NOT NULL,
    DateAdded    date NOT NULL,
    SupplierID   int NOT NULL,
    UnitsOnOrder int NOT NULL,
    FOREIGN KEY (YarnID)
        REFERENCES YarnProduct (YarnID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (BeadID)
        REFERENCES BeadProduct (BeadID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (PaintID)
        REFERENCES PaintProduct (PaintID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (SupplierID)
        REFERENCES Suppliers (SupplierID)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Reviews
(
    ReviewID      int AUTO_INCREMENT PRIMARY KEY,
    ProductID     int,
    Username      varchar(50) NOT NULL,
    Photos        varchar(100),
    Rating        int         NOT NULL,
    WrittenReview varchar(500),
    FOREIGN KEY(ProductID)
        REFERENCES Products(ProductID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Username)
        REFERENCES Customers (Username)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Projects
(
    ProjectID    int PRIMARY KEY AUTO_INCREMENT,
    Username     varchar(50)  NOT NULL,
    Hobby        varchar(100) NOT NULL,
    Hours        numeric      NOT NULL,
    ReviewID     int,
    Photos       varchar(100),
    ProductsUsed int,
    FOREIGN KEY (Username)
        REFERENCES Customers (Username)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ReviewID)
        REFERENCES Reviews (ReviewID),
    FOREIGN KEY (ProductsUsed)
        REFERENCES Products (ProductID)
);

CREATE TABLE IF NOT EXISTS Patterns
(
    ProjectID     int PRIMARY KEY AUTO_INCREMENT,
    Name          varchar(100) NOT NULL,
    Username      varchar(50)  NOT NULL,
    Difficulty    int          NOT NULL,
    EstimatedTime numeric,
    Material      int,
    FOREIGN KEY (ProjectID)
        REFERENCES Projects (ProjectID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Material)
        REFERENCES Products (ProductID),
    FOREIGN KEY (Username)
        REFERENCES Customers (Username)
);

CREATE TABLE IF NOT EXISTS Orders
(
    OrderID    int PRIMARY KEY AUTO_INCREMENT,
    CustomerID int                             NOT NULL,
    OrderDate  date                           NOT NULL,
    Price      numeric                            NOT NULL,
    FOREIGN KEY (CustomerID)
        REFERENCES Customers (CustomerID)
);

CREATE TABLE IF NOT EXISTS OrderDetails
(
    OrderID   int PRIMARY KEY,
    UnitPrice numeric NOT NULL,
    Products  int  NOT NULL,
    Quantity  int     NOT NULL,
    Discount  numeric NOT NULL,
    FOREIGN KEY (OrderID)
        REFERENCES Orders (OrderID),
    FOREIGN KEY (Products)
        REFERENCES Products (ProductID)
);

CREATE TABLE IF NOT EXISTS Shipments
(
    OrderID         int PRIMARY KEY,
    ShippingAddress varchar(100) NOT NULL,
    Carrier         varchar(100) NOT NULL,
    TrackingID      int UNIQUE   NOT NULL AUTO_INCREMENT,
    FOREIGN KEY (OrderID)
        REFERENCES Orders (OrderID)
);


SELECT * FROM Projects