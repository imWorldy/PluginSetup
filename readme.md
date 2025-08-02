# Plugin Setup - Rapid Spigot/Paper Plugin Environment

A powerful tool to quickly set up a Minecraft Spigot/Paper plugin development environment with an integrated server for testing.

## Features

- 🚀 Create a complete Spigot/Paper plugin project structure
- ⚡ Set up a local Minecraft server for testing
- 🔧 Automatic Maven configuration
- 📦 Easy plugin packaging and deployment
- 🌍 Cross-platform support (Windows, macOS, Linux)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- Java Development Kit (JDK) 8 or 17 (recommended for newer Minecraft versions)
- Maven (for building the plugin)

### Installing Prerequisites

#### Windows
1. **Python**:
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"

2. **Java JDK**:
   - Download from [Adoptium](https://adoptium.net/)
   - Run the installer and follow the instructions
   - Verify installation by opening Command Prompt and typing:
     ```
     java -version
     javac -version
     ```

3. **Maven**:
   - Download from [Maven website](https://maven.apache.org/download.cgi)
   - Extract the archive to a directory (e.g., `C:\Program Files\Apache\maven`)
   - Add Maven's `bin` directory to your system's PATH environment variable
   - Verify installation by opening a new Command Prompt and typing:
     ```
     mvn -v
     ```

#### macOS
1. **Using Homebrew (recommended)**:
   ```bash
   # Install Homebrew if you don't have it
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python, Java, and Maven
   brew install python openjdk@17 maven
   ```

2. **Verify installations**:
   ```bash
   python3 --version
   java -version
   mvn -v
   ```

#### Linux (Debian/Ubuntu)
```bash
# Update package list
sudo apt update

# Install Python 3
sudo apt install python3 python3-pip

# Install OpenJDK 17
sudo apt install openjdk-17-jdk

# Install Maven
sudo apt install maven

# Verify installations
python3 --version
java -version
mvn -v
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/imWorldy/PluginSetup
   cd PluginSetup
   ```

## Configuration

1. Edit the `config.py` file to set the path to your Paper/Spigot server JAR:
   ```python
   # Put here the path to your Paper/Spigot server.jar
   # You can download Paper from https://papermc.io/downloads
   SERVER_JAR = r"path\to\your\paper-1.20.1.jar"
   ```

## Usage

1. Run the generator:
   ```bash
   # Windows
   python main.py
   
   # macOS/Linux
   python3 main.py
   ```

2. Follow the interactive prompts:
   - Enter a name for your plugin (or type 'skip' to skip plugin creation)
   - Specify the target folder for your project
   - Enter a Java package name (e.g., com.yourname.pluginname) or 'skip'

3. The script will:
   - Create a complete Maven project structure
   - Set up a basic plugin template
   - Configure a local Minecraft server for testing
   - Create start scripts

## Running Your Plugin

1. Navigate to your server directory:
   ```bash
   cd path/to/your/project/server
   ```

2. Start the server:
   - **Windows**: Double-click `start.bat` or run it from the command line
   - **macOS/Linux**: Run `./start.sh` (you might need to make it executable first with `chmod +x start.sh`)

3. The first time you start the server, it will generate necessary files and shut down. You'll need to:
   - Edit `eula.txt` and change `eula=false` to `eula=true`
   - Start the server again

4. Your plugin will be automatically built and placed in the `plugins` folder

## Project Structure

```
your-project/
├── pom.xml                 # Maven configuration
├── src/
│   └── main/
│       ├── java/           # Java source files
│       │   └── com/
│       │       └── yourname/
│       │           └── pluginname/
│       │               └── YourPlugin.java
│       └── resources/      # Resource files
│           └── plugin.yml  # Plugin configuration
└── server/                 # Minecraft server files
    ├── server.jar
    ├── start.bat
    ├── start.sh
    ├── eula.txt
    └── plugins/
        └── yourplugin-1.0.jar
```

## Building Your Plugin

To manually build your plugin:

1. Navigate to your project directory
2. Run:
   ```bash
   mvn clean package
   ```
3. The compiled plugin will be in the `target` directory

## Troubleshooting

### Maven not found
- Make sure Maven is installed and added to your system's PATH
- On Windows, you might need to restart your terminal/IDE after installation

### Java version issues
- Ensure you have the correct Java version installed
- For Minecraft 1.17+, you need Java 16 or higher
- For older versions, Java 8 is recommended

### Server startup issues
- Make sure you've accepted the EULA by editing `eula.txt`
- Check the server logs for specific error messages
- Ensure no other application is using the default port (25565)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [SpigotMC](https://www.spigotmc.org/)
- [PaperMC](https://papermc.io/)
- [Maven](https://maven.apache.org/)