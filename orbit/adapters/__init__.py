# orbit/adapters/__init__.py

"""
Adaptadores externos para Orbit.
Incluye soporte para configuración heredada y cifrado híbrido con claves externas.
"""

from orbit.adapters.base import BaseProjectAdapter
from orbit.adapters.security import HybridSecurityAdapter

__all__ = [
    "BaseProjectAdapter",
    "HybridSecurityAdapter"
]
