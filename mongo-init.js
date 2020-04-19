db.createUser(
    {
        user: "root",
        pwd: "23052019",
        roles: [
            {
                role: "root",
                db: "seismic-test"
            }
        ]
    }
);
