using System.ComponentModel.DataAnnotations;

namespace Models
{
    public class UpdateUserModel
    {
        [Required]
        public string Name { get; set; }
        
        [Required]
        [EmailAddress]
        public string Email { get; set; }
        
        [Required]
        public string Password { get; set; }
    }
}