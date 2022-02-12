using System;

namespace Models
{
    public record Teacher
    {
        public Guid Id { get; init; }
        public string Name { get; set; }
        public string Department { get; set; }
        public string OrganizationName { get; set; }
        public string AboutMe { get; set; }
    }
}