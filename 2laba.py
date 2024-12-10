from PIL import Image
import os

def get_image_info(file_path):
    try:
        with Image.open(file_path) as img:
            info = {
                "Имя файла": os.path.basename(file_path),
                "Размер (пиксели)": f"{img.width} x {img.height}",
                "Разрешение (dpi)": img.info.get('dpi', 'N/A'),
                "Глубина цвета": img.mode,
                "Сжатие": img.info.get('compression', 'N/A')
            }
            return info
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except OSError:
        print(f"Ошибка открытия файла (не изображение или поврежден): {file_path}")
    except Exception as e:
        print(f"Неизвестная ошибка при обработке {file_path}: {e}")
    return None

def load_images(folder):
    image_info_list = []
    if not os.path.isdir(folder):
        print("Указанная папка не существует.")
        return image_info_list

    for file_name in os.listdir(folder):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.tif', '.bmp')):
            file_path = os.path.join(folder, file_name)
            info = get_image_info(file_path)
            if info:
                image_info_list.append(info)
    return image_info_list

def display_image_info(image_info_list):
    if not image_info_list:
        print("Нет изображений для отображения.")
        return

    print(f"{'Имя файла':<30} {'Размер (пиксели)':<20} {'Разрешение (dpi)':<20} {'Глубина цвета':<20} {'Сжатие':<15}")
    print("=" * 105)
    for info in image_info_list:
        print(f"{info['Имя файла']:<30} {info['Размер (пиксели)']:<20} {info['Разрешение (dpi)']:<20} {info['Глубина цвета']:<20} {info['Сжатие']:<15}")

# Пример использования
folder_path = "ваша_папка"  # Укажите путь к папке с изображениями
image_info = load_images(folder_path)
display_image_info(image_info)
