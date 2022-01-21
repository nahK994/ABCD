using System.ComponentModel.DataAnnotations;

namespace Models
{
    public record UpdateStudentModel
    {
        [Required]
        public string RegNo { get; set; }
        [Required]
        public string Name { get; set; }
        [Required]
        public string OrgName { get; set; }
        [Required]
        public string AboutMe { get; set; }
        [Required]
        public string DeptName { get; set; }
    }
}