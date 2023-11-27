class DecisionDomainService:
    @staticmethod
    def get_decision(temperature: float):
        if temperature < 0:
            return 'Don''t go outside today'
        elif temperature < 20:
            return 'Take a sweater with you'
        else:
            return 'Nice weather to go outside today'
