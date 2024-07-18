
def auto_save_txt(str_buffer, log_file = r'C:\Users\42418\Desktop\2024ldjs\EnglishMulu\auto_test\overall_result.txt'):
    file = open(log_file, 'a')
    file.write(str_buffer + '\n')
    file.close()
    return 0