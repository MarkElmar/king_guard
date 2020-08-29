CREATE TABLE IF NOT EXISTS kingdom_roles(
    role_id INT NOT NULL AUTO_INCREMENT,
    role VARCHAR(50) NOT NULL,
    PRIMARY KEY(role_id)
);

INSERT INTO kingdom_roles (role)
    VALUES
        ('King'),
        ('Queen'),
        ('Prince'),
        ('Princess'),
           ('Duke'),
           ('Duchess')

