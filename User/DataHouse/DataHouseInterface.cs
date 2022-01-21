using System;
using Models;
using System.Collections.Generic;

namespace DataHouse
{
    public interface DataHouseInterface
    {
        User getUser(Guid Id);
        List<User> getUsers();
        Guid createUser(User User);
        void updateUser(User User);
        void deleteUser(User User);
    }
}