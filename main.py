import yaml
from deserialize_json import DeserializeJson
from serialize_json import SerializeJson
from convert_json_to_yaml import ConvertJsonToYaml
print("hey, it's me - Python!")
tempconffile = open('Assets/basic_config.yaml', encoding="utf8")
confdata = yaml.load(tempconffile, Loader=yaml.FullLoader)
newDeserializator = DeserializeJson(confdata['paths']['source_folder'] + confdata['paths']['json_source_file'])
end = False
while(end == False):
    print("Wybierz co chcesz zrobic:")
    print("1-wypisanie liczby urzedów dla poszczególncy województw")
    print("2-serializacja danych")
    print("3-konwersja na yaml")
    print("4-zakończ działanie programu")
    wybor = int(input('Podaj swój wybór:'))
    match wybor:
        case 1:
            newDeserializator.somestats()
        case 2:
            print("Wybierz zródło serializacji:")
            print("1-plik")
            print("2-obiekt")
            wybor2 = int(input("Podaj swój wybor:"))
            match wybor2:
                case 1:
                    SerializeJson.run(confdata['paths']['source_folder'] + confdata['paths']['json_source_file'],
                                      confdata['paths']['source_folder'] + confdata['paths']['json_destination_file'])
                case 2:
                    SerializeJson.run(newDeserializator,
                               confdata['paths']['source_folder'] + confdata['paths']['json_destination_file'])
                case _:
                    print("Nie bylo takiego wyboru !")
        case 3:
            print("Wybierz zródło:")
            print("1-plik")
            print("2-obiekt")
            wybor3 = int(input("Podaj swój wybór:"))
            match wybor3:
                case 1:
                    ConvertJsonToYaml.run(confdata['paths']['source_folder'] + confdata['paths']['json_source_file'],
                                          confdata['paths']['source_folder'] + confdata['paths'][
                                              'yaml_destination_file'])
                case 2:
                    ConvertJsonToYaml.run(newDeserializator,
                                  confdata['paths']['source_folder'] + confdata['paths'][
                                      'yaml_destination_file'])
                case _:
                    print("Nie było takiego wyboru!")
        case 4:
            end = True
            print("Do widzenia")
        case _:
            print("Nie było takiego wyboru !")


