using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using Models;
using DataHouse;

namespace Controller
{
    [ApiController]
    [Route("user")]
    public class UsersController: ControllerBase
    {
        DataHouseInterface DataHouseInterface;
        public UsersController(DataHouseInterface DataHouseInterface)
        {
            this.DataHouseInterface = DataHouseInterface;
        }

        [HttpGet("/get")]
        public List<User> getUsers()
        {
            return DataHouseInterface.getUsers();
        }

        [HttpGet("/get/{Id}")]
        public ActionResult<User> getUser(Guid Id)
        {
            User User = DataHouseInterface.getUser(Id);
            if(User is null)
            {
                NotFound();
            }

            return Ok(User);
        }

        [HttpPut("/put/{Id}")]
        public ActionResult updateUser(UpdateUserModel updateUserModel, Guid Id)
        {
            User user = DataHouseInterface.getUser(Id);
            if(User is null)
            {
                return NotFound();
            }

            User updatedUser = user with {
                Name = updateUserModel.Name,
                Email = updateUserModel.Email
            };
            DataHouseInterface.updateUser(updatedUser);

            return NoContent();
        }

        [HttpPost("/create")]
        public Guid createUser(CreateUserModel createUserModel)
        {
            User user = new(){
                Id = Guid.NewGuid(),
                Name = createUserModel.Name,
                Email = createUserModel.Email,
                Password = createUserModel.Password
            };

            DataHouseInterface.createUser(user);

            return user.Id;
        }

        [HttpDelete("/delete/{Id}")]
        public ActionResult deleteUser(Guid Id)
        {
            User user = DataHouseInterface.getUser(Id);
            if(user is null)
            {
                return NotFound();
            }

            DataHouseInterface.deleteUser(user);
            return NoContent();
        }
    }
}