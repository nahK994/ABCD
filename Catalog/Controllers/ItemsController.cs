using Microsoft.AspNetCore.Mvc;
using Catalog.Repositories;
using System;
using Catalog.Dtos;
using System.Collections.Generic;
using Catalog.Entity;

namespace Catalog.Controller
{
    [ApiController]
    [Route("items")]
    public class ItemsController: ControllerBase
    {
        readonly ItemRepositories ItemRepositories;
        public ItemsController(ItemRepositories ItemRepositories)
        {
            this.ItemRepositories = ItemRepositories;
        }

        [HttpGet("/get")]
        public List<GetItemDto> GetItems()
        {
            return ItemRepositories.GetItems().AsDtos();
        }

        [HttpGet("/get/{id}")]
        public ActionResult<GetItemDto> GetItem(Guid id)
        {
            var item = ItemRepositories.GetItem(id).AsDto();
            if(item is null)
            {
                return NotFound();
            }

            return Ok(item);
        }

        [HttpPost("/post")]
        public Guid PostItem(CommandItemDto commansGetItemDto)
        {
            Guid Guid = Guid.NewGuid();
            Item item = new Item{
                Id = Guid,
                Name = commansGetItemDto.Name,
                Price = commansGetItemDto.Price,
                CreatedDate = DateTimeOffset.UtcNow
            };
            ItemRepositories.PostItem(item);

            return Guid;
        }

        [HttpPut("/put/{id}")]
        public ActionResult PutItem(UpdateItemDto updateGetItemDto, Guid id)
        {
            Item item = ItemRepositories.GetItem(id);
            if(item is null)
            {
                return NotFound();
            }
            Item updatedItem = item with {
                Name = updateGetItemDto.Name,
                Price = updateGetItemDto.Price
            };
            ItemRepositories.PutItem(updatedItem);
            return NoContent();
        }

        [HttpDelete("/delete/{id}")]
        public void DeleteItem(Guid id)
        {
            ItemRepositories.DeleteItem(id);
        }
    }
}