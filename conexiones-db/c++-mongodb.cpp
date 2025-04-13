#include <mongocxx/client.hpp>
#include <mongocxx/instance.hpp>
#include <mongocxx/uri.hpp>
#include <iostream>

int main() {
    mongocxx::instance inst{};
    mongocxx::client conn{mongocxx::uri{"mongodb://localhost:27017"}};

    auto db = conn["mi_base"];
    auto collection = db["mi_coleccion"];

    std::cout << "Conectado a MongoDB" << std::endl;
}
