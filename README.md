## django-app
SImple django application

## MOngoDb guidance

Summary of command mongo database in order to interact with database

### Create database
``use database
``
### create collection
``db.createCollection('collectionName')
``
### insert in collection
- insert one line
```
db.collectionName.insertOne({
    field: "value",(string value)
    field: value,(integer value)
    field: ["news", "events"],(array value
    field: Date() (date value)
    field: {
        field: value,
        field: value
    }( dic value)
})
```
- insert many line
```

db.collectionName.insertMany(
    {
    field: "value",(string value)
    field: value,(integer value)
    field: ["news", "events"],(array value
    field: Date() (date value)
    field: {
        field: value,
        field: value
    }( dic value)
},{
    field: "value",(string value)
    field: value,(integer value)
    field: ["news", "events"],(array value
    field: Date() (date value)
    field: {
        field: value,
        field: value
    }( dic value)
},{
    field: "value",(string value)
    field: value,(integer value)
    field: ["news", "events"],(array value
    field: Date() (date value)
    field: {
        field: value,
        field: value
    }( dic value)
}
)
```



