using Catalog.Entity;
using System;
using System.Linq;
using System.Collections.Generic;
using Catalog.Dtos;

namespace Catalog.Repositories
{
    public class InMemItemRepositories: ItemRepositories
    {
        private readonly List<Item> items = new() {
            new Item { Id = Guid.NewGuid(), Name = "Speaker", Price = 12, CreatedDate = DateTimeOffset.UtcNow },
            new Item { Id = Guid.NewGuid(), Name = "Laptop", Price = 20, CreatedDate = DateTimeOffset.UtcNow },
            new Item { Id = Guid.NewGuid(), Name = "Calculator", Price = 35, CreatedDate = DateTimeOffset.UtcNow }
        };

        public Item GetItem(Guid Id)
        {
            return items.Where(item => item.Id == Id).SingleOrDefault();
        }

        public List<Item> GetItems()
        {
            return items;
        }

        public void PostItem(Item item)
        {
            items.Add(item);
        }

        public void PutItem(Item Item)
        {
            int index = items.FindIndex(item => item.Id == Item.Id);
            items[index] = new Item{
                CreatedDate = Item.CreatedDate,
                Id = Item.Id,
                Name = Item.Name,
                Price = Item.Price
            };
        }
        public void DeleteItem(Guid Id)
        {
            int index = items.FindIndex(item => item.Id == Id);
            items.RemoveAt(index);
        }
    }
}