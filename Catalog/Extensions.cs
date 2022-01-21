using Catalog.Dtos;
using Catalog.Entity;
using System.Collections.Generic;

namespace Catalog
{
    public static class Extensions
    {
        public static GetItemDto AsDto(this Item item)
        {
            return new GetItemDto{
                Id = item.Id,
                Name = item.Name,
                Price = item.Price,
                CreatedDate = item.CreatedDate
            };
        }

        public static List<GetItemDto> AsDtos(this List<Item> items)
        {
            List<GetItemDto> list = new();
            for(int i=0 ; i<items.Count ; i++)
            {
                list.Add(Extensions.AsDto(items[i]));
            }
            return list;
        }
    }
}