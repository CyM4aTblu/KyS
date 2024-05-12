import re
class ReplaceService:
    @staticmethod
    def replace_e(text:str) -> str:
        return re.sub(r'ё', 'е', text)

    @staticmethod
    def replace_i(text:str) -> str:
        return re.sub(r'й', 'и', text)

    @staticmethod
    def replace_e_by_count(text: str, count: int) -> str:
        return re.sub(r'ё', 'е', text, count)

    @staticmethod
    def replace_i_by_count(text: str, count: int) -> str:
        return re.sub(r'й', 'и', text, count)