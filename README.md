# Crafters' Eden Database
## MySQL + Flask Boilerplate Project

Do you love crafting but don’t want to support a big-box crafts chain? We have a database for you! Using this database, small crafts suppliers can post different types of yarn, beads, or paints for purchase. Then, all types of consumers can view information about said craft supply such as price per unit, average user rating, and distributors with in-stock inventory. They could also browse through craft-specific attributes such as yardage per skein, needle/hook size, weight, fiber, color, bead radius, net count, materials/ingredients, and fluid volume. Consumers also have the option of posting and viewing projects that other consumers have completed with a certain craft supply.



This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 




