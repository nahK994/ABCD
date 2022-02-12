using System.ComponentModel.DataAnnotations;

namespace Models
{
    public class CreateStudentEventModel
    {
        [Required]
        public string Name { get; set; }

        [Required]
        public string StudentId { get; set; }
        
        [Required]
        [EmailAddress]
        public string Department { get; set; }
        
        [Required]
        public string OrganizationName { get; set; }

        [Required]
        public string AboutMe { get; set; }
    }
}