using Catalog.Entity;
using System;
using System.Collections.Generic;
using Catalog.Dtos;

namespace Catalog.Repositories
{
    public interface ItemRepositories
    {
        List<Item> GetItems();
        Item GetItem(Guid Id);
        void PostItem(Item Item);
        void PutItem(Item item);
        void DeleteItem(Guid Id);
    }
}