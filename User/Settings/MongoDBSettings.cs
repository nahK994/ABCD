namespace Setings
{
    public class MongoDbSettings
    {
        public string Host { get; set; }
        public string Port { get; set; }

        public string ConnectionSettings
        {
            get {
                return $"mongodb://{Host}:{Port}";
            }
        }
    }
}