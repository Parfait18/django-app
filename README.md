## django-app
SImple django application

## MOngoDb guidance

Summary of command mongo database in order to interact with database

### Create database
``use database
``
### Create collection
``db.createCollection('collectionName')
``
### Insert in collection
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
### Find data in collection
- find all data which match with my condition
```
db.collectionName.find({
    category : 'value'
})
```
- find all data which match with my condition and display the title and date fields in the results
```
db.collection.find({
    {(for condition)},
    { data:1, title: 1, _id:0}

})
```
 We use a `` 1 `` to include a field and `` 0 `` to exclude a field.
- find one element
``
db.collectionName.findOne()
``
