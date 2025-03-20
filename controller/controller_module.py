
class RunwayManager:
    def allocate_runway(self, aircraft):
        for idx, status in enumerate(self. runways):
            if status == 'free':
                self.runways[idx] = 'occupied'
                return idx # ID przydzielonego pasa
        return None # Brak wolnych pasów

