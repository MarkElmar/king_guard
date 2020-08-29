CREATE TABLE IF NOT EXISTS player_roles(
    player_id bigint NOT NULL,
    kingdom_id int NOT NULL,
    role_id int NOT NULL,
    PRIMARY KEY (player_id, kingdom_id)
)