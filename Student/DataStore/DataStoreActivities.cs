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
        private const string CollectionName = "Students";
        private readonly IMongoCollection<Student> StudentsCollection;
        private readonly FilterDefinitionBuilder<Student> filterBuilder = Builders<Student>.Filter;
        public DataStoreActivities(IMongoClient mongoClient)
        {
            IMongoDatabase mongoDatabase = mongoClient.GetDatabase(DatabaseName);
            StudentsCollection = mongoDatabase.GetCollection<Student>(CollectionName);
        }
        public Student getStudent(Guid Id)
        {
            var filter = filterBuilder.Eq(item => item.Id, Id);
            return StudentsCollection.Find(filter).SingleOrDefault();
        }
        public List<Student> getStudents()
        {
            return StudentsCollection.Find(new BsonDocument()).ToList();
        }
        public Guid createStudent(Student Student)
        {
            StudentsCollection.InsertOne(Student);
            return Student.Id;
        }
        public void updateStudent(Student Student)
        {
            var filter = filterBuilder.Eq(item => item.Id, Student.Id);
            StudentsCollection.ReplaceOne(filter, Student);
        }
        public void deleteStudent(Student Student)
        {
            var filter = filterBuilder.Eq(item => item.Id, Student.Id);
            StudentsCollection.DeleteOne(filter);
        }
    }
}