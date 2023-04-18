DROP SCHEMA IF EXISTS crafterseden ;
CREATE SCHEMA IF NOT EXISTS crafterseden;
USE crafterseden;

#  drop table YarnProduct, BeadProduct, PaintProduct, Products,
#     Projects, Patterns, Reviews, Orders, OrderDetails, Customers, Suppliers, Shipments;

CREATE TABLE IF NOT EXISTS Suppliers
(
    SupplierID bigint PRIMARY KEY AUTO_INCREMENT,
    Location   varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Customers
(
    CustomerID bigint PRIMARY KEY AUTO_INCREMENT,
    Name       varchar(100) NOT NULL,
    Email      varchar(100) NOT NULL UNIQUE,
    Address    varchar(100) NOT NULL,
    Phone      varchar(15)  NOT NULL UNIQUE,
    Username   varchar(50)  NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS YarnProduct
(
    YarnID               bigint PRIMARY KEY AUTO_INCREMENT,
    ProductName          varchar(100) NOT NULL,
    SkeinLength          numeric      NOT NULL,
    Price                numeric      NOT NULL,
    Fiber                varchar(100) NOT NULL,
    Color                varchar(50)  NOT NULL,
    YarnWeight           varchar(100) NOT NULL,
    NetWeight            numeric      NOT NULL,
    Brand                varchar(100) NOT NULL,
    ManufacturingCountry varchar(100) NOT NULL,
    Photos               blob
);

CREATE TABLE IF NOT EXISTS BeadProduct
(
    BeadID               bigint PRIMARY KEY AUTO_INCREMENT,
    ProductName          varchar(100) NOT NULL,
    Material             varchar(100) NOT NULL,
    Price                numeric      NOT NULL,
    Color                varchar(50)  NOT NULL,
    Size                 numeric      NOT NULL,
    Brand                varchar(100) NOT NULL,
    ManufacturingCountry varchar(100) NOT NULL,
    Photos               blob
);

CREATE TABLE IF NOT EXISTS PaintProduct
(
    PaintID              bigint PRIMARY KEY AUTO_INCREMENT,
    ProductName          varchar(100) NOT NULL,
    Base                 varchar(100) NOT NULL,
    Ingredients          varchar(500) NOT NULL,
    Price                numeric      NOT NULL,
    Color                varchar(50)  NOT NULL,
    FluidVolume          numeric      NOT NULL,
    Brand                varchar(100) NOT NULL,
    ManufacturingCountry varchar(100) NOT NULL,
    Photos               blob
);

CREATE TABLE IF NOT EXISTS Products
(
    ProductID    bigint PRIMARY KEY AUTO_INCREMENT,
    YarnID       bigint,
    BeadID       bigint,
    PaintID      bigint,
    UnitsInStock int NOT NULL,
    DateAdded    datetime DEFAULT CURRENT_TIMESTAMP,
    SupplierID   bigint NOT NULL,
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
    ReviewID      bigint AUTO_INCREMENT,
    ProductID     bigint
    Username      varchar(50) NOT NULL,
    Photos        blob,
    Rating        int         NOT NULL,
    WrittenReview varchar(500),
    PRIMARY KEY(ReviewID, ProductID)
    FOREIGN KEY(ProductID)
        REFERENCES Products(ProductID)
        ON UPDATE CASCADE ON DELETE CASCADE
    FOREIGN KEY (Username)
        REFERENCES Customers (Username)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Projects
(
    ProjectID    bigint PRIMARY KEY AUTO_INCREMENT,
    Username     varchar(50)  NOT NULL,
    Hobby        varchar(100) NOT NULL,
    Hours        numeric      NOT NULL,
    ReviewID     bigint,
    Photos       blob,
    ProductsUsed bigint,
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
    ProjectID     bigint PRIMARY KEY AUTO_INCREMENT,
    Name          varchar(100) NOT NULL,
    Username      varchar(50)  NOT NULL,
    Difficulty    int          NOT NULL,
    EstimatedTime numeric,
    Material      bigint,
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
    OrderID    bigint PRIMARY KEY AUTO_INCREMENT,
    CustomerID bigint                             NOT NULL,
    OrderDate  datetime                           NOT NULL,
    Price      numeric                            NOT NULL,
    FOREIGN KEY (CustomerID)
        REFERENCES Customers (CustomerID)
);

CREATE TABLE IF NOT EXISTS OrderDetails
(
    OrderID   bigint PRIMARY KEY,
    UnitPrice numeric NOT NULL,
    Products  bigint  NOT NULL,
    Quantity  int     NOT NULL,
    Discount  numeric NOT NULL,
    FOREIGN KEY (OrderID)
        REFERENCES Orders (OrderID),
    FOREIGN KEY (Products)
        REFERENCES Products (ProductID)
);

CREATE TABLE IF NOT EXISTS Shipments
(
    OrderID         bigint PRIMARY KEY,
    ShippingAddress varchar(100) NOT NULL,
    Carrier         varchar(100) NOT NULL,
    TrackingID      bigint UNIQUE   NOT NULL AUTO_INCREMENT,
    FOREIGN KEY (OrderID)
        REFERENCES Orders (OrderID)
);

