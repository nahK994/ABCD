using System;

namespace Models
{
    public record Teacher
    {
        public Guid Id { get; init; }
        public string OrgName { get; set; }
        public string DeptName { get; set; }
        public string AboutMe { get; set; }
    }
}