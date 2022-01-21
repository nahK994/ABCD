using System;
using System.Collections.Generic;
using Models;
using MongoDB.Bson;
using MongoDB.Driver;

namespace DataStore
{
    public class DataStoreActivities: DataStoreInterface
    {
        private const string DatabaseName = "ABCD";
        private const string CollectionName = "Teachers";
        private readonly IMongoCollection<Teacher> teachersCollection;
        private readonly FilterDefinitionBuilder<Teacher> filterBuilder = Builders<Teacher>.Filter;
        public DataStoreActivities(IMongoClient mongoClient)
        {
            IMongoDatabase mongoDatabase = mongoClient.GetDatabase(DatabaseName);
            teachersCollection = mongoDatabase.GetCollection<Teacher>(CollectionName);
        }
        public Teacher getTeacher(Guid Id)
        {
            var filter = filterBuilder.Eq(item => item.Id, Id);
            return teachersCollection.Find(filter).SingleOrDefault();
        }
        public List<Teacher> getTeachers()
        {
            return teachersCollection.Find(new BsonDocument()).ToList();
        }
        public Guid createTeacher(Teacher Teacher)
        {
            teachersCollection.InsertOne(Teacher);
            return Teacher.Id;
        }
        public void updateTeacher(Teacher Teacher)
        {
            var filter = filterBuilder.Eq(item => item.Id, Teacher.Id);
            teachersCollection.ReplaceOne(filter, Teacher);
        }
        public void deleteTeacher(Teacher Teacher)
        {
            var filter = filterBuilder.Eq(item => item.Id, Teacher.Id);
            teachersCollection.DeleteOne(filter);
        }
    }
}