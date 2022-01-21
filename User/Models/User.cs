using System;

namespace Models
{
    public record User
    {
        public Guid Id { get; init; }
        public String Name { get; set; }
        public String Email { get; set; }
        public String Password { get; set; }
    }
}