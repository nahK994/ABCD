using System.ComponentModel.DataAnnotations;
using System;

namespace Catalog.Dtos
{
    public record DeleteItemDto
    {
        [Required]
        public Guid Id { get; set; }
    }
}