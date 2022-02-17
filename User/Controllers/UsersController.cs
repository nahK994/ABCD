using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using Models;
using DataHouse;
using MassTransit;
using System.Threading.Tasks;

namespace Controller
{
    [ApiController]
    [Route("user")]
    public class UsersController: ControllerBase
    {
        DataHouseInterface DataHouseInterface;
        private readonly IBus _bus;
        public UsersController(DataHouseInterface DataHouseInterface, IBus bus)
        {
            this.DataHouseInterface = DataHouseInterface;
            _bus = bus;
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

        [HttpPost("/create/test")]
        public async Task<ActionResult> createUserTestAsync()
        {
            CreateTeacherEventModel TeacherEventModel = new CreateTeacherEventModel{
                Name = "Shomi Khan",
                AboutMe = "I am always awesome cool",
                DepartmentName = "EEE",
                OrganizationName = "SUST"
            };

            Uri uri = new Uri("rabbitmq://localhost/ticketQueue");
            var endPoint = await _bus.GetSendEndpoint(uri);
            await endPoint.Send(TeacherEventModel);
            Console.WriteLine("check");
            return Ok();
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