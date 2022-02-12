using System.ComponentModel.DataAnnotations;

namespace Models
{
    public record UpdateTeacherModel
    {
        [Required]
        public string Name { get; set; }
        [Required]
        // [EmailAddress]
        public string DepartmentName { get; set; }
        
        [Required]
        public string OrganizationName { get; set; }

        [Required]
        public string AboutMe { get; set; }
    }
}