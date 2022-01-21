using System;
using Models;
using System.Collections.Generic;
using MongoDB.Bson;
using MongoDB.Driver;

namespace DataHouse
{
    public class DataHouseActivities: DataHouseInterface
    {
        private const string DatabaseName = "ABCD";
        private const string CollectionName = "Users";
        private readonly IMongoCollection<User> usersCollection;
        private readonly FilterDefinitionBuilder<User> filterBuilder = Builders<User>.Filter;
        public DataHouseActivities(IMongoClient mongoClient)
        {
            IMongoDatabase mongoDatabase = mongoClient.GetDatabase(DatabaseName);
            usersCollection = mongoDatabase.GetCollection<User>(CollectionName);
        }
        public User getUser(Guid Id)
        {
            var filter = filterBuilder.Eq(item => item.Id, Id);
            return usersCollection.Find(filter).SingleOrDefault();
        }
        public List<User> getUsers()
        {
            return usersCollection.Find(new BsonDocument()).ToList();
        }
        public Guid createUser(User User)
        {
            usersCollection.InsertOne(User);
            return User.Id;
        }
        public void updateUser(User User)
        {
            var filter = filterBuilder.Eq(item => item.Id, User.Id);
            usersCollection.ReplaceOne(filter, User);
        }
        public void deleteUser(User User)
        {
            var filter = filterBuilder.Eq(item => item.Id, User.Id);
            usersCollection.DeleteOne(filter);
        }
    }
}