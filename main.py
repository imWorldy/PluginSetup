import os
import subprocess
import urllib.request
import shutil
from config import SERVER_JAR


def safe_write(path, content):
    if os.path.exists(path):
        print(f"⚠️  File already exists, skipping: {path}")
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"✅ File created: {path}")

def create_server(server_path):
    plugins_path = os.path.join(server_path, "plugins")
    os.makedirs(plugins_path, exist_ok=True)

    # Fixed path to server.jar on your PC
    source_jar = SERVER_JAR
    target_jar = os.path.join(server_path, "server.jar")

    if not os.path.exists(source_jar):
        print(f"❌ Error: Source server.jar not found at:\n{source_jar}")
        return

    if not os.path.exists(target_jar):
        shutil.copy(source_jar, target_jar)
        print(f"✅ server.jar was copied to:\n{target_jar}")
    else:
        print("📄 server.jar already exists in the project, skipping.")

    safe_write(os.path.join(server_path, "start.bat"), "java -Xmx2G -Xms2G -jar server.jar nogui\npause\n")
    safe_write(os.path.join(server_path, "eula.txt"), "eula=true")

    print(f"\n✅ Server fully set up at:\n{server_path}")

def create_plugin(plugin_name, base_path, package_name):
    MAIN_CLASS = plugin_name.replace("-", "")
    SPIGOT_VERSION = "1.8.8-R0.1-SNAPSHOT"
    JAVA_VERSION = "8"

    java_path = os.path.join(base_path, "src/main/java", package_name.replace('.', '/'))
    resource_path = os.path.join(base_path, "src/main/resources")
    plugins_path = os.path.join(base_path, "server/plugins")

    for d in [java_path, resource_path, plugins_path]:
        os.makedirs(d, exist_ok=True)

    # Create Java class
    safe_write(os.path.join(java_path, f"{MAIN_CLASS}.java"), f"""package {package_name};

import org.bukkit.plugin.java.JavaPlugin;

public class {MAIN_CLASS} extends JavaPlugin {{

    @Override
    public void onEnable() {{
        getLogger().info("{plugin_name} Plugin enabled!");
    }}

    @Override
    public void onDisable() {{
        getLogger().info("{plugin_name} Plugin disabled.");
    }}
}}
""")

    # Create plugin.yml
    safe_write(os.path.join(resource_path, "plugin.yml"), f"""name: {plugin_name}
version: 1.0
main: {package_name}.{MAIN_CLASS}
api-version: 1.8.8
""")

    # Create pom.xml
    safe_write(os.path.join(base_path, "pom.xml"), f"""<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>{package_name}</groupId>
    <artifactId>{plugin_name}</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>{JAVA_VERSION}</maven.compiler.source>
        <maven.compiler.target>{JAVA_VERSION}</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <repositories>
        <repository>
            <id>spigot-repo</id>
            <url>https://hub.spigotmc.org/nexus/content/repositories/snapshots/</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>org.spigotmc</groupId>
            <artifactId>spigot-api</artifactId>
            <version>{SPIGOT_VERSION}</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.3.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals><goal>shade</goal></goals>
                        <configuration>
                            <outputFile>{plugins_path}/{plugin_name}-1.0.jar</outputFile>
                            <minimizeJar>true</minimizeJar>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
""")

    print("📦 Plugin structure created. Building plugin with Maven...")

    # Build plugin using Maven
    subprocess.run(["mvn", "clean", "package"], cwd=base_path, shell=True)
    print(f"✅ Plugin was built and is located at: {plugins_path}")

# ───────────────────────────────
# Main program

print("\n🧙‍♂️ Spigot Plugin Generator with integrated Server Setup")


plugin_name = input("🔤 Plugin name (e.g. test1 or 'skip' to skip plugin creation): ").strip()
target_folder = input("📁 Target folder for project: ").strip()
package_name = input("📦 Java package name (e.g. test1.test2.test3) or 'skip': ").strip()

base_path = os.path.join(target_folder, plugin_name if plugin_name.lower() != "skip" else "project")

if plugin_name.lower() != "skip" and package_name.lower() != "skip":
    create_plugin(plugin_name, base_path, package_name)
else:
    print("⏭️  Plugin creation skipped.")

create_server(os.path.join(base_path, "server"))
