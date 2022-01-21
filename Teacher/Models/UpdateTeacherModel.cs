using System.ComponentModel.DataAnnotations;

namespace Models
{
    public record UpdateTeacherModel
    {
        [Required]
        public string OrgName { get; set; }
        [Required]
        public string DeptName { get; set; }
        [Required]
        public string AboutMe { get; set; }
    }
}