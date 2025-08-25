

// 3)

db.tweets.aggregate([
    {
      $group: {
        _id: "$user.screen_name",
        "total_tweets": {
          $sum: 1,
        },
      },
    },
    {
      $sort: {
        "total_tweets": -1,
      },
    },
  ]);


// 4)

db.tweets.aggregate([
    {
      $group: {
        _id: "$place.name",
        "total_tweets": {
          $sum: 1,
        },
      },
    },
    {
      $sort: {
        "total_tweets": -1,
      },
    },
  ]);
  


// 5)


db.tweets.aggregate([
  {
    $group: {
      _id: "$in_reply_to_screen_name",
      "total_replies_tweets": {
        $sum: 1,
      },
    },
  },
  {
    $sort: {
      "total_replies_tweets": -1,
    },
  },
]);


// 6)

db.tweets.aggregate([
  
  // {
  //   $match: {
  //   "entities.hashtags": {$ne: [],}
  //   },
  // },
  {
    $unwind:
      {
        path: "$entities.hashtags",
      },
  },
  {
    $group: {
      _id: "$user.screen_name",
      num_hashtags: {
        $sum: 1,
      },
    },
  },
  {
    $sort: {
      num_hashtags: -1,
    },
  },
]).pretty()