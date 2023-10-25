## django-app
SImple django application

## MongoDb guidance

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
### Update collection
- update collection which match with condition
```
db.collectionName.updateOne(
    {title : "value"(condition)},
    { $set: {field: "value"} }(update))
```
- insert new data if not found
```
db.collectionName.updateOne(
    {title : "value"(condition)},
    { $set: {field: "value"} },(update)
    {upsert: true}
    )
```
- update all data in collection who match with condition
```
db.collectionName.updateMany(
    { title : "value"(condition),
    { $inc: { field: value}}}
)

```
### Delete data from collection
- delete first element which match with condition
```
db.collectionName.deleteOne(
    {title : "value"(condition)},
    )
```
- delete all elements of collection which match with collection 
```
db.collectionName.deleteMany(
    {title : "value"(condition)},
    )

```
## Query operator
### Comparaison
- `` $eq `` : value are equal
- `` $ne `` : value are not equal
- `` $gt `` : value is greater than another
- `` $gte `` : value is greater or equal than another
- `` $lt `` : value is less than another
- `` $lte `` : value is less or equal than another
- `` $in `` : Value is matched within an array

### Logical
- `` $and `` : return documents wher both query match
- `` $or `` : return documents where one of both query match
- `` $nor ``: return documents where both query fail to match
- `` $not `` : return documents where query does not match 

### Evaluation
- `` $regex `` : allow use of regular expressions for field evalutation


## Aggrégation Pipeline
Aggregation operations allow you to group, sort, perform calculations, analyze data, and much more.

Aggregation pipelines can have one or more "stages". The order of these stages are important. Each stage acts upon the results of the previous stage.

### aggregation example of use
```
db.collectionName.aggregate(
    [
        // Stage 1: Only find documents that match condition  
        {
           $match: {field : { $gt: 1}} (condition example)
        }  ,
       // Stage 2: Group documents by category and sum each categories likes (exmaple)
       {
       $group : {
           _id: "$category", 
           totalLikes:{ $sum : "$likes" }
            }
       }
    ]
)
```
### $group
This aggregation stage groups documents by the unique ``_id`` expression provided.
```
db.collectionName.aggregate([
    {
        $group: { _id: "field_want_to_group_by_name"}
    }
])
```

### $limit
This aggregation stage limits the number of documents passed to the next stage. 
```
db.collectionName.aggregate([
    { $limit: 1}
])
```

### $project
This aggregation stage passes only the specified fields along to the next aggregation stage.

```
db.collectionName.aggregate([
  {
    //display only name, cuisine and address field
    $project: {
      "name": 1,
      "cuisine": 1,
      "address": 1
      "_id": 0 // exclud _id field
    }
  },
  //limit resutl for 5 element
  {
    $limit: 5
  }
])

```
### $sort
This aggregation stage groups sorts all documents in the specified sort or

```
db.collectionName.aggregate(
    [
        { $sort: { "field_want_to_sort": 1 }}
    ]
)
```
The sort order can be chosen by using `` 1 `` or `` -1 ``. `` 1 `` is **ascending** and `` -1 `` is **descending**. 


### $match
``` 
db.collectionName.aggregate([
    { $match: { field: "value"}}
])
```
### $addFields
This aggregation stage adds new fields to documents.
```
db.collectionName.aggregate([
    { 
        addFields: {
            avgScore: { $avg: "$grades.score"}
        }
    }
])

```

### $count
This aggregation stage counts the total amount of documents passed from the previous stage.
``` 
db.collectionName.aggregate([
    { $match: { field: "value"}}
    { $count: "totalChiness"}
])
```
