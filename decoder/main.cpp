
#include "Test1.pb.h"
#include <string>

using std::string;

namespace{
    void print(const string& stream)
    {
        size_t size = stream.size();
        printf("stream size = %zu\n", size);
        for(size_t i = 0; i < size; i++)
        {
            if(i != size - 1)
                printf("0X%02X,", stream[i]);
            else
                printf("0X%02X\n", stream[i]);
        }
    }
}

int main()
{
    Test1 test1;
    test1.set_a(105);
    test1.PrintDebugString();
    print(test1.SerializeAsString());

    return 0;
}
