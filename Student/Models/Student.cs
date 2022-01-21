using System;

namespace Models
{
    public record Student
    {
        public Guid Id { get; init; }
        public string RegNo { get; set; }
        public string Name { get; set; }
        public string OrgName { get; set; }
        public string AboutMe { get; set; }
        public string DeptName { get; set; }
    }
}