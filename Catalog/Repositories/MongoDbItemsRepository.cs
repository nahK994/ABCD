using System;
using System.Collections.Generic;
using Catalog.Entity;
using MongoDB.Bson;
using MongoDB.Driver;

namespace Catalog.Repositories
{
    public class MongoDbItemsRepository: ItemRepositories
    {
        private const string DatabaseName = "Catalog";
        private const string CollectionName = "Items";
        private readonly IMongoCollection<Item> itemsCollection;
        private readonly FilterDefinitionBuilder<Item> filterBuilder = Builders<Item>.Filter;
        public MongoDbItemsRepository(IMongoClient mongoClient)
        {
            IMongoDatabase mongoDatabase = mongoClient.GetDatabase(DatabaseName);
            itemsCollection = mongoDatabase.GetCollection<Item>(CollectionName);
        }
        public List<Item> GetItems()
        {
            return itemsCollection.Find(new BsonDocument()).ToList();
        }
        public Item GetItem(Guid Id)
        {
            var filter = filterBuilder.Eq(item => item.Id, Id);
            return itemsCollection.Find(filter).SingleOrDefault();
        }
        public void PostItem(Item Item)
        {
            itemsCollection.InsertOne(Item);
        }
        public void PutItem(Item item)
        {
            var filter = filterBuilder.Eq(item => item.Id, item.Id);
            itemsCollection.ReplaceOne(filter, item);
        }
        public void DeleteItem(Guid Id)
        {
            var filter = filterBuilder.Eq(item => item.Id, Id);
            itemsCollection.DeleteOne(filter);
        }
    }
}