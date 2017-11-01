use video;

db.movieDetails.findOne({
  "year": 2013,
  "rated": "PG-13",
  "awards.wins": {"$lt":1}},
  {"title": 1, "_id": 0
});
