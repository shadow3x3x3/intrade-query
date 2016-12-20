class PackageManager:
    FILE_PATH = 'query/packages_list/old.txt'

    def __init__(self):
        self.package_ids = set()

    def __str__(self):
        return self.package_ids

    def add(self, id):
        self.package_ids.add(id)
        self._write(id)

    def update(self):
        self.package_ids.clear()
        with open(self.FILE_PATH) as file:
            for line in file:
                self.package_ids.add(line)

    def context(self):
        return { 'packages': self.package_ids }

    def _write(self, id):
        with open(self.FILE_PATH, 'a') as file:
            file.write('\n{}'.format(id))