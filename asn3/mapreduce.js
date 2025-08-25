

// 7)

function myHashTagMapper() {
    //The mapper function is called with each document, which has the special name 'this'
    //Emit a key-value pair:
    //(the mapper can emit many key-value pairs if needed)
    // emit(this.user.screen_name, 1);
    for (hashtag of this.entities.hashtags) {
        emit(hashtag.text, 1);
    }
}

function myHashTagReducer(key, values) {
    //The reducer is called once for each key, and is passed an array
    //containing all values corresponding to that key.
    //Produce the desired result
    return Array.sum( values );
}


db.tweets.mapReduce(myHashTagMapper, myHashTagReducer, { query: {}, out: "mroutput" })
db.mroutput.aggregate({$sort: {value: -1}})


// db.mroutput.aggregate([
//     { $sort: { value: -1 } }, 
//     { $project: { value: 1, total: "$value" } } // Project the fields to rename "value" to "total"
// ]);

