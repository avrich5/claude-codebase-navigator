# FF

**Категория:** 💰 [DeFi & Crypto Tools](../categories/defi_crypto.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/FF`

## 📁 Files (7 indexed)

### Code (4 files, 3.0 MB)

| File | Size | Modified |
|------|------|----------|
| `fitness-function-4.ipynb` | 337 KB | 2024-05-17 |
| `fitness-function-3.ipynb` | 58 KB | 2024-05-14 |
| `fitness-function copy.ipynb` | 482 KB | 2024-05-14 |
| `fitness-function.ipynb` | 2.2 MB | 2024-05-14 |

### Docs (2 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `readme.md` | 8 KB | 2024-06-06 |
| `FF ФФ.txt` | 478 B | 2024-05-22 |

### Config (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `.vscode/launch.json` | 531 B | 2024-05-14 |

## 📝 README

```
# Конфигурация

Этот файл описывает параметры конфигурации, используемые в проекте.

## Параметры конфигурации

### env

#### Основные параметры
В этой секции перечислены основные параметры, необходимые для настройки окружения.

- **ASSET**: `string` - Название актива, используемого в стратегии (например, "XRP"). 🔴
- **T_ASSET**: `string` - Название тестового актива (например, "TXRP").
- **FITNESS_VERSION**: `string` - Версия функции фитнеса.
- **CROSSOVER_VERSION**: `string` - Версия кроссинговера.

#### Параметры мутации
Эти параметры управляют процессом мутации генетического алгоритма.

- **MUTATION_RATE**: `number` - Скорость мутаций в алгоритме. 🔴
- **PERCENT_OF_CHANGES**: `number` - Процент изменений в популяции. 🔴
- **MUTATION_DEGREE**: `number` - Степень мутаций. 🔴

#### Параметры популяции
Эти параметры определяют размеры популяции и элиты.

- **INITIAL_POPULATION_SIZE**: `number` - Начальный размер популяции. 🔴
- **INITIAL_ELITE_SIZE**: `number` - Начальный размер элиты. 🔴
- **ELITE_SIZE**: `number` - Размер элиты. 🔴
- **AFTER_CROSSOVER_SIZE**: `number` - Размер популяции после кроссинговера. 🔴
- **TEST_ELITE_SIZE**: `number` - Размер тестовой элиты. 🔴
- **GENERATIONS**: `number` - Количество поколений. 🔴

#### Параметры сетки и родительской глубины

- **MAX_GRID_POS**: `number` - Максимальная позиция в сетке. 🔴
- **MAX_PARENT_DEPTH_FOR_STABILITY_FITNESS**: `number` - Максимальная глубина родителей для стабильности фитнеса. 🔴
- **PARENT_DEPTH_FOR_ELITE**: `number` -
```
